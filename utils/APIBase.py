from playwright.sync_api import Playwright

payload_create_order = {"orders": [{"country": "India","productOrderedId": "68a961459320a140fe1ca57a"}]}
payload_token_generate = {"userEmail": "sudhirsu17@gmail.com","userPassword": "13579@RahulShettyAcademy"}

class APIUtils:
    def generate_token(self, playwright:Playwright):
        req_new_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        login_response = req_new_context.post(url="/api/ecom/auth/login",
                                              data=payload_token_generate,
                                              headers={"Content-Type": "application/json"})
        print(login_response.json())
        login_response_dict = login_response.json()
        return login_response_dict["token"]


    def create_order(self, playwright:Playwright):
        token = self.generate_token(playwright)
        req_new_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        create_order_response = req_new_context.post(url="/api/ecom/order/create-order",
                             headers={"Authorization": token,
                                      "Content-Type": "application/json"},
                             data=payload_create_order)

        print(create_order_response.json())
        response_body = create_order_response.json()
        order_id = response_body["orders"][0]
        return order_id
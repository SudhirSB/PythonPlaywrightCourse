pipeline {
    agent any

    parameters {
        choice(
            name: 'BROWSER',
            choices: ['all', 'chrome', 'firefox', 'webkit'],
            description: 'Select the browser to run tests on or "all" to run in parallel'
        )
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (params.BROWSER == 'all') {
                        parallel(
                            'Chrome Tests': { bat 'python -m pytest -n 3 --browser_name chrome --html=report_chrome.html --tracing on --reruns 2' },
                            'Firefox Tests': { bat 'python -m pytest -n 3 --browser_name firefox --html=report_firefox.html --tracing on --reruns 2' },
                            'Webkit Tests': { bat 'python -m pytest -n 3 --browser_name webkit --html=report_webkit.html --tracing on --reruns 2' }
                        )
                    } else {
                        bat "python -m pytest -n 3 --browser_name ${params.BROWSER} --html=report.html --tracing on --reruns 2"
                    }
                }
            }
            post {
                always {
                    script {
                        if (params.BROWSER == 'all') {
                            publishHTML([reportName: 'Chrome Report', reportDir: '.', reportFiles: 'report_chrome.html', keepAll: true])
                            publishHTML([reportName: 'Firefox Report', reportDir: '.', reportFiles: 'report_firefox.html', keepAll: true])
                            publishHTML([reportName: 'Webkit Report', reportDir: '.', reportFiles: 'report_webkit.html', keepAll: true])
                        } else {
                            publishHTML([reportName: "${params.BROWSER} Report", reportDir: '.', reportFiles: 'report.html', keepAll: true])
                        }
                    }
                }
            }
        }

    }
}

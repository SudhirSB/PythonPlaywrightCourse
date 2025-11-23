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
                bat 'playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (params.BROWSER == 'all') {
                        parallel(
                            'Chrome Tests': { bat 'python -m pytest -n 3 --browser_name chrome --html=report_chrome.html --tracing on' },
                            'Firefox Tests': { bat 'python -m pytest -n 3 --browser_name firefox --html=report_firefox.html --tracing on' },
                            'Edge Tests': { bat 'python -m pytest -n 3 --browser_name edge --html=report_edge.html --tracing on' }
                        )
                    } else {
                        bat "python -m pytest -n 3 --browser_name ${params.BROWSER} --html=report.html --tracing on --reruns 2"
                    }
                }
            }
        }

        stage('Publish HTML Report') {
            steps {
                script {
                    if (params.BROWSER == 'all') {
                        publishHTML([reportName: 'Chrome Report', reportDir: '.', reportFiles: 'report_chrome.html', keepAll: true])
                        publishHTML([reportName: 'Firefox Report', reportDir: '.', reportFiles: 'report_firefox.html', keepAll: true])
                        publishHTML([reportName: 'Edge Report', reportDir: '.', reportFiles: 'report_edge.html', keepAll: true])
                    } else {
                        publishHTML([reportName: "${params.BROWSER} Report", reportDir: '.', reportFiles: 'report.html', keepAll: true])
                    }
                }
            }
        }

    }
}

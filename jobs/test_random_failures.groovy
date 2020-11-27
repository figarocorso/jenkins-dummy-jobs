job = pipelineJob("Test_Random_Failures")
job.with {
    description('Execute a test suite that shuld have random failures')
    logRotator {
        daysToKeep(100)
        numToKeep(100)
    }
    properties {
        pipelineTriggers {
            triggers {
                cron {
                    spec("*/10 * * * *")
                }
            }
        }
    }

    definition {
        cps {
            script(readFileFromWorkspace('src/main/resources/pipelines/test_random_failures.pipeline'))
        }
    }
}

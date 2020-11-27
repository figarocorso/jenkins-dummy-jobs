job = pipelineJob("Test_All_right")
job.with {
    description('Execute a test suite that always succeeds')
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
            script(readFileFromWorkspace('src/main/resources/pipelines/test_all_right.pipeline'))
        }
    }
}

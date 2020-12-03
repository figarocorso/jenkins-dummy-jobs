job = pipelineJob("Random-sleep-Random-success")
job.with {
    description('Execute every 10 minutes. Wait for some random 1..20 seconds and success, unstable or fail randomly')
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
            script(readFileFromWorkspace('src/main/resources/pipelines/random_sleep_random_success.pipeline'))
            sandbox(true)
        }
    }
}

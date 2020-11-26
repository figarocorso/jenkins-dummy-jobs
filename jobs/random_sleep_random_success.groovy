job = pipelineJob("Random-sleep-Random-success")
job.with {
    description('Execute every minute. Wait for some random 1..10 seconds and success, unstable or fail randomly')
    logRotator {
        daysToKeep(100)
        numToKeep(100)
    }
    properties {
    pipelineTriggers {
        triggers {
            cron {
                spec("*/1 * * * *")
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

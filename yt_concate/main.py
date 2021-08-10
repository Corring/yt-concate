from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    # 这段程式码是在运行每个steps
    # this is a pipeline
    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


# 如果是进入点才执行这个function
if __name__ == '__main__':
    main()

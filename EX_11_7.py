from datetime import datetime


class Case:

    def __init__(self, case_: dict) -> None:
        self.case_ = case_

    def retrieve_seconds(self) -> None:
        if self.case_['end_task'] is None:
            print("Task not finished yet")
        else:
            delta_time = datetime.fromisoformat(self.case_['end_task']) - \
                         datetime.fromisoformat(self.case_['created_task'])
            print(delta_time.total_seconds())


def main():

    first_case = {
        'name': 'first_case',
        'created_task': '2021-10-26T19:48:12+00:00',
        'end_task': None
    }
    second_case = {
        'name': 'second_case',
        'created_task': '2021-09-26T19:48:12+00:00',
        'end_task': '2021-10-26T19:48:12+00:00'
    }
    test_case = {
        'name': 'second_case',
        'created_task': '2021-09-26T19:48:12+00:00',
        'end_task':     '2021-09-27T19:48:12+00:00'
    }

    case1 = Case(first_case)
    case1.retrieve_seconds()
    case2 = Case(second_case)
    case2.retrieve_seconds()

    # test 1 day = 24*60*60 = 86400
    case3 = Case(test_case)
    case3.retrieve_seconds()


if __name__ == "__main__":
    main()

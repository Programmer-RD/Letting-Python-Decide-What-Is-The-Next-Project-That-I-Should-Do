import time
import random
import os


def make_prediction(projects, last_projects, numberofiternations):
    times = numberofiternations
    print(times)
    file_name = f"todo-projects {times + random.randint(0,times) + random.randint(0,times) + random.randint(0,times) + random.randint(0,times)+ random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times) +random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times)+random.randint(0,times) }.txt"
    with open(
        file_name,
        "w",
    ) as a:
        a.write("")
    total_random_nums = []
    for x in range(times):
        random_nums = []
        for m in range(times):
            for o in range(random.randint(0, 5)):
                random_nums.append(random.randint(0, len(projects)))
        total_random_nums.append(random_nums)
    with open(file_name, "w") as a:
        for p in range(times):
            for x in total_random_nums:
                for m in x:
                    if m < len(projects):
                        a.write(projects[m])
                        a.write("\n")
                        del projects[projects.index(projects[m])]
    with open(file_name, "a") as q:
        q.write(last_projects[1])
        q.write("\n")
        q.write(last_projects[0])
    with open(file_name, "r") as b:
        results = b.read()
        print("Getting Results....")
    with open(f"times.text", "a") as a:
        a.write(f"{times} \n")
    return results


def a():
    number_of_times = 10000
    print(number_of_times)
    a = 30
    for x in range(number_of_times):
        projects = [
            "Amazon Clone",
            "Instergram Clone",
            "Covid19 Clone",
            "Youtube Clone",
            "TikTok Clone",
            "Spotify Clone",
            "Twitter Clone",
            "Slack Clone",
            "Instergram Reels Clone",
            "Whatsup Clone",
            "Google Clone",
            "Facebook Clone",
            "Airbnb Clone",
            "Hulu Clone",
        ]
        last_projects = ["iMessage Clone", "Discord 	Clone"]
        result = make_prediction(
            projects=projects,
            last_projects=last_projects,
            numberofiternations=random.randint(0, a),
        )
        print(result)


def b():
    FINAL_RESULTS = []
    for x in range(50):
        arr = os.listdir()
        del arr[arr.index("Random.py")]
        info = []
        info_index = []
        for x in arr:
            with open(x, "r") as a:
                info.append(a.read())
                info_index.append(arr.index(x))
        results = []
        for x in range(10000):
            results.append(info[random.randint(0, len(info_index) - 1)])
        results_2 = []
        for x in range(5000):
            results_2.append(results[random.randint(0, len(results)) - 1])
        results_3 = []
        for x in range(2500):
            results_3.append(results[random.randint(0, len(results_2)) - 1])
        results_4 = []
        for x in range(1250):
            results_4.append(results[random.randint(0, len(results_3)) - 1])
        FINAL_RESULTS.append(results_4[random.randint(0, len(results_4)) - 1])
    finalist_results = []
    for x in range(10000):
        finalist_results.append(
            FINAL_RESULTS[random.randint(0, len(FINAL_RESULTS)) - 1]
        )
    results____ = finalist_results[random.randint(0, len(finalist_results)) - 1]
    return results____


def test():
    all_ = []
    sss = []
    for x in range(5):
        print(f"1 {x}")
        for x in range(2):
            print(f"2 {x}")
            for x in range(5):
                print(f"3 {x}")
                result = b()
                all_.append(result)
            sss.append(all_[random.randint(0, len(all_)) - 5 + 2])
    return sss


def x():
    result = test()
    for x in result:
        print("\n")
        print(x)
        print("\n")


def pl():
    for pop in range(5):
        x()


a = [
    "Instergram Clone",
    "Amazon Clone",
    "Covid19 Tracker",
    "Youtube Clone",
    "Tik Tok Clone",
    "Spotfy Clone",
    "Twitter Clone",
    "Slack Clone",
    "Intergram Reels Clone",
    "Whatsapp Clone",
    "Google Clone",
    "Facebook Clone",
    "Airbnb Clone",
    "Hulu Clone",
    "Discord Clone",
    "iMessage Clone",
]
#

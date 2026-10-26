from app import Owner, Pet, CareTask, PetScheduler


def test_high_priority_first():
    owner = Owner("Jordan", 120, "08:00")
    pet = Pet("Mochi", "dog")

    scheduler = PetScheduler(owner, pet)

    tasks = [
        CareTask("Grooming", 30, "low"),
        CareTask("Feeding", 10, "high"),
    ]

    schedule, skipped = scheduler.generate_schedule(tasks)

    assert schedule[0]["Task"] == "Feeding"


def test_time_limit():
    owner = Owner("Jordan", 20, "08:00")
    pet = Pet("Mochi", "dog")

    scheduler = PetScheduler(owner, pet)

    tasks = [
        CareTask("Morning walk", 30, "high"),
        CareTask("Feeding", 10, "high"),
    ]

    schedule, skipped = scheduler.generate_schedule(tasks)

    assert len(schedule) == 1
    assert schedule[0]["Task"] == "Feeding"
    assert len(skipped) == 1


def test_empty_tasks():
    owner = Owner("Jordan", 120, "08:00")
    pet = Pet("Mochi", "dog")

    scheduler = PetScheduler(owner, pet)

    schedule, skipped = scheduler.generate_schedule([])

    assert schedule == []
    assert skipped == []
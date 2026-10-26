# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system firsst (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```text
Daily Plan for Mochi (dog)

Owner: Jordan
Available Time: 120 minutes
Schedule Start Time: 08:00 AM

08:00 AM — Feeding (10 min) [priority: high]
08:10 AM — Grooming (30 min) [priority: low]

Why These Tasks?

Feeding: Selected because this task has high priority and fits within the available time.

Grooming: Selected because this task has low priority and fits within the available time.
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```text
tests/test_scheduler.py::test_high_priority_first PASSED
tests/test_scheduler.py::test_time_limit PASSED
tests/test_scheduler.py::test_empty_tasks PASSED

================ 3 passed in 0.78s ================
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `generate_schedule()` | Sorts tasks by priority (high, medium, low) and duration. |
| Filtering | `generate_schedule()` | Skips tasks that exceed the available time. |
| Conflict handling | `generate_schedule()` | Schedules tasks sequentially to avoid overlapping time slots. |
| Recurring tasks | Not implemented | Daily and weekly recurring tasks can be added in the future. |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. Open the PawPal+ application using Streamlit. The homepage displays the title and introduction to the pet care scheduling assistant.
2. Enter the owner's information, including name, available time, and schedule start time.
3. Enter the pet's information, including pet name and species.
4. Add pet care tasks such as feeding, walking, and grooming. Enter the duration and priority for each task and click "Add Task."
5. Click "Generate Schedule" to create a daily pet care plan. The application displays the tasks with their start times, end times, durations, and priorities.
6. Review the "Why These Tasks?" section to understand why each task was selected. Tasks that cannot fit within the available time are shown as skipped.

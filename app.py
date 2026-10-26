import streamlit as st
from dataclasses import dataclass
from datetime import datetime, timedelta


# -----------------------------
# CLASSES
# -----------------------------

@dataclass
class Owner:
    name: str
    available_minutes: int
    start_time: str


@dataclass
class Pet:
    name: str
    species: str


@dataclass
class CareTask:
    title: str
    duration_minutes: int
    priority: str


# -----------------------------
# SCHEDULING LOGIC
# -----------------------------

class PetScheduler:

    PRIORITY_ORDER = {
        "high": 0,
        "medium": 1,
        "low": 2
    }

    def __init__(self, owner, pet):
        self.owner = owner
        self.pet = pet

    def generate_schedule(self, tasks):
        ordered_tasks = sorted(
            tasks,
            key=lambda task: (
                self.PRIORITY_ORDER[task.priority],
                task.duration_minutes
            )
        )

        schedule = []
        skipped = []

        remaining = self.owner.available_minutes

        current_time = datetime.strptime(
            self.owner.start_time, "%H:%M"
        )

        for task in ordered_tasks:

            if task.duration_minutes <= remaining:

                start = current_time

                end = start + timedelta(
                    minutes=task.duration_minutes
                )

                explanation = (
                    f"Selected because this task has "
                    f"{task.priority} priority and fits "
                    f"within the available time."
                )

                schedule.append({
                    "Task": task.title,
                    "Start": start.strftime("%I:%M %p"),
                    "End": end.strftime("%I:%M %p"),
                    "Duration": task.duration_minutes,
                    "Priority": task.priority,
                    "Explanation": explanation
                })

                remaining -= task.duration_minutes
                current_time = end

            else:
                skipped.append({
                    "Task": task.title,
                    "Reason": "Not enough available time"
                })

        return schedule, skipped


# -----------------------------
# STREAMLIT APP
# -----------------------------

st.set_page_config(
    page_title="PawPal+",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 PawPal+")

st.write(
    "Your personal pet care scheduling assistant!"
)

st.markdown(
    "Plan your pet's daily activities based on "
    "priority and available time."
)

st.divider()


# -----------------------------
# OWNER INFORMATION
# -----------------------------

st.header("👤 Owner Information")

owner_name = st.text_input(
    "Owner name",
    value="Jordan"
)

available_minutes = st.number_input(
    "Available time today (minutes)",
    min_value=1,
    max_value=1440,
    value=120
)

start_time = st.time_input(
    "Schedule start time",
    value=datetime.strptime("08:00", "%H:%M").time()
)


# -----------------------------
# PET INFORMATION
# -----------------------------

st.header("🐶 Pet Information")

pet_name = st.text_input(
    "Pet name",
    value="Mochi"
)

species = st.selectbox(
    "Species",
    ["dog", "cat", "other"]
)


# -----------------------------
# TASK MANAGEMENT
# -----------------------------

st.header("📋 Pet Care Tasks")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "schedule" not in st.session_state:
    st.session_state.schedule = None

if "skipped" not in st.session_state:
    st.session_state.skipped = []

task_title = st.text_input(
    "Task title",
    value="Morning walk"
)

duration = st.number_input(
    "Duration (minutes)",
    min_value=1,
    max_value=240,
    value=20
)

priority = st.selectbox(
    "Priority",
    ["high", "medium", "low"]
)

if st.button("➕ Add Task"):

    if task_title.strip():

        new_task = CareTask(
            title=task_title.strip(),
            duration_minutes=int(duration),
            priority=priority
        )

        st.session_state.tasks.append(new_task)

        st.session_state.schedule = None

        st.success("Task added successfully!")

    else:
        st.error("Please enter a task title.")


# -----------------------------
# VIEW AND EDIT TASKS
# -----------------------------

if st.session_state.tasks:

    st.subheader("Current Tasks")

    for index, task in enumerate(st.session_state.tasks):

        with st.expander(
            f"{task.title} ({task.priority})"
        ):

            new_title = st.text_input(
                "Edit title",
                value=task.title,
                key=f"title_{index}"
            )

            new_duration = st.number_input(
                "Edit duration",
                min_value=1,
                max_value=240,
                value=task.duration_minutes,
                key=f"duration_{index}"
            )

            new_priority = st.selectbox(
                "Edit priority",
                ["high", "medium", "low"],
                index=["high", "medium", "low"].index(
                    task.priority
                ),
                key=f"priority_{index}"
            )

            if st.button(
                "Save Changes",
                key=f"save_{index}"
            ):

                if new_title.strip():

                    st.session_state.tasks[index] = CareTask(
                        new_title.strip(),
                        int(new_duration),
                        new_priority
                    )

                    st.session_state.schedule = None

                    st.success("Task updated!")

                    st.rerun()

                else:
                    st.error("Task title cannot be empty.")

            if st.button(
                "Delete Task",
                key=f"delete_{index}"
            ):

                st.session_state.tasks.pop(index)

                st.session_state.schedule = None

                st.rerun()

else:

    st.info("No tasks yet. Add one above.")


# -----------------------------
# GENERATE SCHEDULE
# -----------------------------

st.divider()

st.header("📅 Daily Pet Care Schedule")

if st.button("🚀 Generate Schedule"):

    if not st.session_state.tasks:

        st.warning(
            "Please add at least one task first."
        )

    else:

        owner = Owner(
            name=owner_name,
            available_minutes=int(available_minutes),
            start_time=start_time.strftime("%H:%M")
        )

        pet = Pet(
            name=pet_name,
            species=species
        )

        scheduler = PetScheduler(owner, pet)

        schedule, skipped = scheduler.generate_schedule(
            st.session_state.tasks
        )

        st.session_state.schedule = schedule
        st.session_state.skipped = skipped


# -----------------------------
# DISPLAY RESULTS
# -----------------------------

if st.session_state.schedule is not None:

    st.subheader(
        f"🐾 Daily Plan for {pet_name}"
    )

    if st.session_state.schedule:

        st.success(
            "Your pet care schedule is ready!"
        )

        st.dataframe(
            st.session_state.schedule,
            use_container_width=True,
            hide_index=True
        )

        st.subheader("🧠 Why These Tasks?")

        for item in st.session_state.schedule:

            st.write(
                f"**{item['Task']}**: "
                f"{item['Explanation']}"
            )

    else:

        st.warning(
            "No tasks fit within the available time."
        )

    if st.session_state.skipped:

        st.subheader("⚠️ Skipped Tasks")

        for item in st.session_state.skipped:

            st.write(
                f"**{item['Task']}** — "
                f"{item['Reason']}"
            )


st.divider()

st.caption(
    "PawPal+ | AI110 Module 2 Project"
)
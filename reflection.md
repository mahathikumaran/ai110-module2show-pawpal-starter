PawPal+ Project Reflection

1. System Design

a. Initial design

Briefly describe your initial UML design.

What classes did you include, and what responsibilities did you assign to each?

My initial UML design included four classes: Owner, Pet, CareTask, and PetScheduler. The Owner class stores the owner's name, available time, and schedule start time. The Pet class stores the pet's name and species, while CareTask stores the task title, duration, and priority. PetScheduler is responsible for organizing tasks and generating a daily schedule.

b. Design changes

Did your design change during implementation?

If yes, describe at least one change and why you made it.

Yes, my design changed slightly during implementation. I originally planned to have a general Scheduler class, but I implemented it as PetScheduler to make its purpose clearer. I also added explanations for scheduled tasks so users could understand why each activity was selected.

2. Scheduling Logic and Tradeoffs

a. Constraints and priorities

What constraints does your scheduler consider (for example: time, priority, preferences)?

How did you decide which constraints mattered most?

My scheduler considers task priority, duration, available time, and the owner's selected start time. I decided that priority and available time were the most important constraints because essential pet care tasks should be completed first. The scheduler sorts tasks from high to low priority and checks whether each task fits within the remaining time.

b. Tradeoffs

Describe one tradeoff your scheduler makes.

Why is that tradeoff reasonable for this scenario?

One tradeoff is that my scheduler prioritizes important tasks instead of trying to fit the maximum number of tasks into the schedule. This means some shorter, lower-priority tasks might be skipped. I think this is reasonable because important activities like feeding and medication should take priority over less urgent activities.

3. AI Collaboration

a. How you used AI

How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

What kinds of prompts or questions were most helpful?

I used ChatGPT to help design the classes, implement scheduling logic, and write automated tests. AI also helped me understand how to connect the Python scheduling logic to the Streamlit interface. The most helpful prompts were specific requests for code that I could test and explanations of how the scheduling functions worked.

b. Judgment and verification

Describe one moment where you did not accept an AI suggestion as-is.

How did you evaluate or verify what the AI suggested?

One AI suggestion was to test several scheduling behaviors, including priority ordering and time limits. Instead of assuming the suggested code worked, I ran the application and checked the generated schedule myself. I also ran pytest to verify the scheduling behavior. All three tests passed, which gave me more confidence in the implementation.

4. Testing and Verification

a. What you tested

What behaviors did you test?

Why were these tests important?

I tested whether high-priority tasks were scheduled first, whether tasks exceeding the available time were skipped, and whether the scheduler handled an empty task list. I also manually tested adding tasks and generating a daily schedule in Streamlit. These tests were important because they verified the main features of the application.

b. Confidence

How confident are you that your scheduler works correctly?

What edge cases would you test next if you had more time?

I am fairly confident that my scheduler works correctly for basic scheduling situations because all three automated tests passed. I also confirmed that the application generated a schedule with correct start and end times. If I had more time, I would test recurring tasks, overlapping preferred time slots, and scheduling tasks for multiple pets.

5. Reflection

a. What went well

What part of this project are you most satisfied with?

I am most satisfied with getting the scheduling logic connected to the Streamlit interface. It was exciting to see the application generate an actual daily schedule based on the tasks I entered. I also liked that the application explained why each task was selected.

b. What you would improve

If you had another iteration, what would you improve or redesign?

If I had another iteration, I would add recurring tasks and reminders for important activities like feeding and medication. I would also improve the scheduler to support preferred time slots and multiple pets. Another improvement would be moving the scheduling classes into a separate Python file to make the code easier to maintain and test.

c. Key takeaway

What is one important thing you learned about designing systems or working with AI on this project?

One important thing I learned is that planning classes and their responsibilities before coding makes the implementation easier to understand. I also learned that AI can help generate code quickly, but developers still need to review and test the results. Running automated tests helped me verify that the scheduling logic worked instead of simply trusting the AI-generated code.
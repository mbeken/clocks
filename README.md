# Clock Exercise

We are interested in running code of course, but even more in your development process and understanding of Software Development Lifecycle Management.

**Fork this repo, then get to work.** Remember that this is a DevOps team, so make sure your repo reflects that. Spend however much time you feel is reasonable. It doesn’t matter if the project is ‘done’, nothing ever is. **When you’re ready push your changes back to Github and put in a pull request back to the base repo.**

This exercise is not meant to take an excessive amount of time. It is an opportunity for you to demonstrate your skills without the stress of an interview. If you start to run out of time, it’s ok to leave an imaginary team member a TODO list that details all the things you didn’t quite have time to do in order for your solution to go to prod.

If you need clarification, or would like to request additional information, pease reach out to the interviewer by email.

## Scenario

You have just joined a DevOps team. This team lives by DevOps principles and you want to let them know you mean business! This particular team is developing a product that is deployed in a Google Cloud Project.

This sprint, the team has been asked to work on a new feature that depends on being able to calculate the angle between the hands on a clock face. They’ve asked you to write some code to help out with that. This is an IOT project, and they have sensors emitting times at a pretty low frequency (about 10 a minute), and for some reason they need to be processed and stored as angles.

You may need to make some assupmtions, that's OK, just document what they are and move on.

The team loves innovation, so you can use whatever languages and technologies you like to complete this. Approach this problem as if your code will go to production. Whilst we don’t expect the code to be perfect, we are not looking for a hacked together script.

Your solution should offer the rest of the team a way to submit a time and receive an angle in return or store it somewhere. They are little fuzzy on the best way to get this low frequency data to your service, so if you can offer them any hints on that, they’d be really happy.

## How to proceed

**Fork this repo, then get to work.** Remember that this is a DevOps team, so make sure your repo reflects that. Spend however much time you feel is reasonable. It doesn’t matter if the project is ‘done’, nothing ever is. **When you’re ready push your changes back to Github and put in a pull request back to the base repo.**

Be sure to add in instructions for how to deploy your solution, and document things in a way that the rest of the team can pick this up and run with it. Remember you have all the tools in the GCP arsenal at your disposal.

We are looking for you to demonstrate your abilities in software practices and DevOps, including reusability, portability, reliability, ease of maintenance etc.

Think about how this will actually be deployed and maintained in the future as you build on it and expand it. You don’t have to implement deployment practices if you don’t have the time or resources, its ok to just document those.

---

## Product Backlog Item (Sprint Story)

Here is the story that is in the backlog. 

As with all stories, the team may have been optimistic with how much can be done in the time permitted. It's ok to meet some of the acceptance criteria by documenting what you would do in the next sprint! Prioritize your time and make sure you have some technical content to deliver.

### Description:-

As a team<br>
We need a serivce that we can send a time value to and have it return or store an angle value<br>
So that we can use it in downstream processing

### Detail:-

We need to calculate the angle between the hands on a clock face. For example input 03:00 would yield 90 degrees.

### Acceptance Criteria:-

1) Code to perform the calculation
1) How will you deploy this solution (in code or as a todo list if time is limited). i.e. how and where will this run?
1) How will you manage any infrastructure needed?
1) Delivered as a feature branch in the repo fork
1) Bonus points for a working deployed solution in GCP that you can demo at the "sprint review" (ie interview)
1) Any DevOps/Cicd components that would support this feature in a production setting

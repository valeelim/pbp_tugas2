# TUGAS 6

## Asynchronous vs Synchronous Programming

Synchronous Programming is a term used for operations that is completed one at a time. In order for one section of the code to be run, you have to wait for the previous sections of the code to finish first.

Asynchronous Programming on the other hand, is a process that simultaneously deals with multiple operations at once. JavaScript itself is a single-threaded asynchronous programming language. Asynchronous process in JavaScript include some common commands for example setTimeout. The way it works is that the call stack sees the command, and sends it back for the Web API, which your browser is responsible for, to run that particular command. After the asynchronous process has finished, your browser would then invoke the callback and basically notify the event loop that you've finished and then run the processes that follows.

## Event-Driven Programming

Event-Driven Programming is a paradigm that focuses more on user interaction to determine the flow of program. The user interacts with the program through what you call `events`. Events could be invoked through multiple actions; clicks, hovers, window resizing, key presses, and so forth. Each event would then be *listened* by the program to run a certain piece of code that the programmer has written. In this project for example, the user interacts a lot with the web app. Whether it may be creating, deleting, or updating, they are all event-driven, and each of those actions would result in something to happen.

## Asynchronous Programming with AJAX

AJAX (Asynchronous JavaScript and XML) allows the client to communicate with the server with the perks of being able to update the web pages asynchronously behind the scenes. That means, the web server doesn't need to reload the entire page when the data exchanged are of a small quantity, but just that bit. This of course optimizes the process of communication between client and server by a ton.

## Implementation

The implementation is a pain to say the least, especially the part where I have to figure out that using `{% url %}` template tag with parameters inside a string literal is almost impossible (I don't know how to do it, if someone knows, please do tell me :blush:).

Since I can't do that, I hardcoded the urls related to each accordion, and that works.

So first of all, I need to get the result from `todolist/json`, so I used `$.get()` to get the data and then for each task I append some HTML to the accordion containers.

To make things easier I made a function that returns the desired accordion based on the template I used in the previous week.

For the `POST`, it's pretty much the same thing, I send the data to the `views` and that handles the database side of things, and on the front end, I just appended the said template. One thing that bothers me though, is that for the newly created tasks, something went wrong with the dates. So I had to copy paste some code from stackoverflow to format the dates accordingly (somehow I did it by setting a default for the date model :innocent:).

I also used a bunch of selectors because each task has their own forms and stuff, and each of them also has some form of id or class. Selecting all of them are painful but necessary since I had to bind them with the appropriate functions.

For the `DELETE`, I used a form that has a method `POST` since forms can't have a `DELETE` method. So basically it has pretty much the same things as the previous methods, I just had to remove the accordion in this one which I did by selecting the accordion and removing it.

I also ended up using jQuery for the checklist toggle thing, since everytime I set a task to finish or the other way around, it would refresh the whole page (I didn't use AJAX before). So I had to do that by again, almost the same code, but here I just added some class and removing some class for each appropriate states.



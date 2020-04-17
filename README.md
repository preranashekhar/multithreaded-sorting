# multithreaded_application
To demonstrate the performance of an application using multi-threads

# Results
For 10 numbers, we see that the single-threaded application takes less time in comparison to a multithreaded program. This is due to the operating system overhead in creating the thread and maintaining the thread. 

<img width="1440" alt="Screen Shot 2020-04-17 at 12 27 25 AM" src="https://user-images.githubusercontent.com/55044852/79545192-23350f00-8045-11ea-9834-fe3cad8dc10e.png">

For 1000 and 10000 numbers:
As we increase the number of elements to be sorted we can see that the multithreaded application takes nearly half of the time taken by a single-threaded system. As the time taken to execute is very small, it is very difficult to notice the difference and hence, a small delay is added to both the applications which help in differentiating the time taken to execute.

<img width="1440" alt="Screen Shot 2020-04-17 at 12 44 12 AM" src="https://user-images.githubusercontent.com/55044852/79545201-27612c80-8045-11ea-8b12-b6b9cb8ecdf6.png">

<img width="1440" alt="Screen Shot 2020-04-17 at 12 42 25 AM" src="https://user-images.githubusercontent.com/55044852/79545200-26c89600-8045-11ea-8709-b35228ebddd3.png">

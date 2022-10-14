# holbertonschool-AirBnB_clone


The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the  [AirBnB website](https://intranet.hbtn.io/rltoken/FrRTcvuF5L9wWDzFE9k01A "AirBnB website").

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

We will have a complete web application composed by:

-   A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
-   A website (the front-end) that shows the final product to everybody: static and dynamic
-   A database or files that store data (data = objects)
-   An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)
- ![enter image description here](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4/20221010/us-east-1/s3/aws4_request&X-Amz-Date=20221010T072521Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=df1c66387017d0515fe21d6d861755bb937682cfc25c063b4405a59b68888182)

# **Description of the project**

This is the first step towards building your first full web application: the  **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

-   put in place a parent class (called  `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
-   create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
-   create all classes used for AirBnB (`User`,  `State`,  `City`,  `Place`…) that inherit from  `BaseModel`
-   create the first abstracted storage engine of the project: File storage.
-   create all unittests to validate all our classes and storage engine

# **Description of the command interpreter:**

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc…
-   Do operations on objects (count, compute stats, etc…)
-   Update attributes of an object
-   Destroy an object
-   ### Execution

Your shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

```

All tests should also pass in non-interactive mode:  `$ echo "python3 -m unittest discover tests" | bash`

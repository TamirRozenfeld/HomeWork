# HomeWork
[Go to Real Cool Heading section](#real-cool-heading)
### 2. Describe the problems that might arise from scaling such a game on one machine.
   The problems that might arise from scaling such a game on one machine could
   be the same problems that happened to me in my last project(Object Detection) when i tried to run the training command,
   it had to run for a long time. With million of bees in all stages moving around, my computer would probably crash, this is why
   clouds/hadoops developed, these apps using maps reduce in order to make things more accesible by using multiple machine
   at the same time and by this making  all the process more efficient and faster.
   more advantage could be that more machines easily added if necessary, And a failure of one machine arn't leading to failure of the entire system
   other machines can still communicate with each other.
   
### 3. Describe the problems that might arise from scaling such a game in a distributed environment.
   1.It is difficult to provide adequate security in distributed systems because the nodes as well as the connections need to be secured.
   2.Some messages and data can be lost in the network while moving from one node to another.
   3.The database connected to the distributed systems is quite complicated and difficult to handle as compared to a single user system.
   4.Overloading may occur in the network if all the nodes of the distributed system try to send data at once.
   
  ###  5. What would the optimization and operations challenges look like if the same game is played online by millions of users at once?
  
  With video games, there is a limited amount of processing power available. An item that is 5km away from the player will require memory and CPU resources to show up on the screen. The game developer will need to decide if rendering something 5km in the distance is worthwhile and if so, is there enough resources to allow for it.
  Draw distance can go on for as long as the system hardware can handle. Larger draw distances will negatively impact the games frame rate.
  The solution for this is to open a game for each area so the CPU and memory will not require too much resources for example a game for only Tel aviv gamers or only in Jerusalem etc..., another solution could be to put a barrier between the players so there will be no need to see each other.

### 6. How would you model & analyze the family lineage tree of a bee
 #####  Description in HB_LifeCycle.
 
   
### 7. How would you design beehive behavior in light of this video:

##### Description in HB_LifeCycle.
   The bees like the robots in the video moves in relation to each other, one bee could activate an algorithm for all others bees and make them start  moving in cohesion for example one bee can find a source of food, she want to tell all the others bees what she had found, she does it by time of waggling, the direction of waggling in relation to the hive indicates direction of the source of food for example 1 second of waggling to the left mean approximately 750m to the left in relation to the hive.
   
   Beehive attacked by bears cause natural response that  make the bees  rise up together and defend their queen just like the robot when its get the command to        move, building a tower or creating the letter K.
   (#real-cool-heading)
  ![Cover_suggestion_1](https://user-images.githubusercontent.com/108065131/185954100-c207e1bc-fcb4-4734-97a0-e3d67f04c9f5.jpg)



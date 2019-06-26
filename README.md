# Starcraft-2-Unit-Recognition

MobileNet has been trained effectively with very low amounts of data, yielding extremely high accuracy with a validation accuracy at 98% and a log loss of 0.0289. This is an extremely surprising and impressive result because each class had very few amounts of training and test data. In comparison Yolo requires a lot more data to effectively train with around 300 images and 31 classes, I could not achieve the a log loss value of (>0.06 according to what the designers of Yolo suggest to be an accurate model). Object detection requires a lot more data than unit recognition but since everything is in place, the result is inevitable.

Currently the only thing I lack are images, to train Yolo for object detection (github contains the commands to run Yolo training and the config file)

Background Information: Starcraft 2 is an extremely fast paced RTS game where players from around the world versus one another to improve in skill and ranking. Starcraft 2 started the era of video game streaming during 2010 to 2012 by dominating the two most popular streaming sites at the time: own3d.tv and twitch.tv formerly known as justin.tv. Twitch.tv is now the most popular US video game streaming site with little competition in it’s way and allows for streamers to interact with the millions of unique viewers that visit the site to watch video game tournaments, ladder climbing matches, speed runs, and many other video game centric content. 
Using deep learning, we can create a model that recognizes Starcraft 2 units and structures as a way to create an interactive stream. If the viewer decides to hover over one of the units that has been recognized by the model, we can display the unit’s details and background information giving unfamiliar viewers a deeper understanding of the game. This model can be used to handle in-game replays, live streams, and other video content. 



 
 This project was to make an obstacle avoidance drone that would attach to the bebop drone.
 
 we used a rasbperry pi 3 B+ and ultrasonic sensors 
 
 for the drone we used the official SDK from the manufacturer 
 
 #### [BebopSample](https://github.com/ARDroneSDK3/Samples/tree/master/Unix/BebopSample)
This example enables you to **connect** to a Bebop drone and **send and receive commands** to pilot it and get its battery level. It also **receives the video stream**. 


In the sdk root folder, you can build the sample:<br/>
`./build.sh -p arsdk-native -t build-sample-BebopSample -j`
Then run it:
`./out/arsdk-native/staging/native-wrapper.sh ./out/arsdk-native/staging/usr/bin/BebopSample`

***We used this code above and the shell commands to build and run the interface to the drone. ***


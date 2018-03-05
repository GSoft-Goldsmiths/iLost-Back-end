var devices;
NRF.findDevices(function(d) {
  devices = d;
  //console.log(devices[0].id);
  //console.log(devices.length);

if (devices[0].id == "c0:97:27:56:81:5d public"){
    console.log("i've found the raspberry pi");
  
  NRF.connect(devices[0].id).then(function(server) {
  // ...
      console.log("i'm connected to the raspberry pi");
    });
  
   }

else if (devices[i].id != "c0:97:27:56:81:5d public"){
     console.log("i can't find the raspberry pi");
    
    //do stuff
    }
  
  
  
  
  
}, 1000);


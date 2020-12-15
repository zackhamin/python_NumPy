var HttpClient = function() {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() { 
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.responseText);
        }
  
        anHttpRequest.open( "GET", aUrl, true );            
        anHttpRequest.send( null );
    }
  }
  
  let apiKey = "d80aa45fc1aa372d7362e2f2e54c0abd";
  let city = "portland";
  
  var client = new HttpClient();
  client.get(`http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`, function(response){
    console.log(response)
  });
  
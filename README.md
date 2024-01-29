**Advice from professional regarding Web scrapping**
Rotate your IPs, 
purchased leases to residential IPs work well, 
and you can set request headers to better imitate a “real” browser instead of whatever WebDriver you’re using. 
A lot of times you can isolate the data call without having to render a bunch of images and just fire that as its own request through postman or whatever and 
then only get the Json for every listing. 
LinkedIn is notoriously tough to do thoroughly though.

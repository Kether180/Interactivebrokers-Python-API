# Getting Started

* You must have Java 8 update 192 or higher installed (gateway is compatible with higher Java versions including OpenJDK 11).

* Download and unzip the CP WebAPI gateway from the website.

* New gateway versions will be released frequently so its recommended to periodically use the gateway download link to download the current version.
Version release notes are under development and will be available in the future.
Navigate to the directory where the gateway has been unzipped in a command prompt.

* Launch the gateway with the command "bin\run.bat root\conf.yaml" (on Windows) or "bin/run.sh root/conf.yaml" (on Mac/Unix).

* To authenticate the gateway session with your account, go to https://localhost:5000/

* The port number is 5000 by default and set in the root/conf.yaml configuration file.
* Authenticate with your username/password and second factor device (for production accounts).

* Note you can login to paper accounts by using the paper account-specific username/password combination. Every paper account has its own username.
The paper account username can be found in Client Portal at: Settings -> Account Settings -> Paper Trading Account -> Configure
You can also reset your paper trading account password there if necessary.

* You should receive the message "Client login succeeds" after successful authentication. The tab can then be closed.

* It is expected that gateway will require restart and reauthentication at least daily.
If left inactive, the gateway session will automatically timeout for security reasons within a few minutes and all endpoints will return 401: Access Denied errors.

* An active session can be extended by pinging the /portal/sso/validate endpoint are regular time intervals, such as once per minute.
Next Steps

* Browse available endpoints

https://www.interactivebrokers.com/api/doc.html

https://interactivebrokers.github.io/cpwebapi/  
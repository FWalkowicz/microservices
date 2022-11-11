# microservices
## Zarys projektu
Naszym celem w tym projekcie jest zbadanie wydajności usług komunikacyjnych wykorzystywanych w środowisku mikroserwisowym. 

Pierwszym zadaniem nad którym będziemy się skupiać będzie budowa 2 [[Mikroserwisy w python|mikroserwisów w pythonie]] na odrębnych komputerach które będą komunikowały się ze sobą za pomocą adresu IP


![Schemat ogólny](https://github.com/FWalkowicz/microservices/blob/main/Badanie%20wydajno%C5%9Bci%20us%C5%82ug%20komunikacyjnych%20w%20%C5%9Brodowisku%20mikroserwisowym%202022-10-25%2019.54.36.excalidraw.png)


### Zadania komunikacyjne
- Przesłanie dużej ilości małych zapytań
- Zapytania do bazy
- Pliki
- Streaming wideo

### Badanie wydajności zapytań względem różnych interfejsów komunikacyjnych
- GRPC
- SOAP
- REST
- MQTT

Po przesłaniu paczki danych będziemy obserwować szybkość działania oraz ile danych było potrzebnych do przesłania w przypadku różnych interfejsów. Po pozyskaniu potrzebnych danych będziemy budować mape wymagań dla których transmisji dane rzeczy były by najbardziej optymalne.

# microservices
## Zarys projektu
Naszym celem w tym projekcie jest zbadanie wydajności usług komunikacyjnych wykorzystywanych w środowisku mikroserwisowym. 

Pierwszym zadaniem nad którym będziemy się skupiać będzie budowa 2 [[Mikroserwisy w python|mikroserwisów w pythonie]] na odrębnych komputerach które będą komunikowały się ze sobą za pomocą adresu IP

>[!info] schemat ogólny
>![[Badanie wydajności usług komunikacyjnych w środowisku mikroserwisowym 2022-10-25 19.54.36.excalidraw|800]]
>
>

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

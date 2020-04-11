Tippelj egyet!
==============

![Licence](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)

## Beállítás
A http_server.py fájlba írjuk bele a hosztnevet, illetve szükség esetén frissítsük a `wsuri` változót.

## Indítás Docker nélkül
```bash
pip3 install flask websockets
python3 http_server.py &
python3 ws_server.py &
```
## Indítás Docker konténerrel
A Docker kép fordítása után az 5000-es porton kapjuk meg a HTTP kérések kiszolgálását, 8765-ös porton a Websocket kérések kiszolgálását.

## Élesítés
A Docker konténert helyezzük egy reverse-proxy mögé, majd lássuk el SSL tanúsítvánnyal. Egy lehetséges és jó megoldás egy Kubernetes klaszterben történő hosztolás.

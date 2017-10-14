# Demo monkeypatch

```
# Magic happened after with!
>>> import mymodule
>>> mymodule.Hello()
Hello, Jacky!
>>> import monkeypatch
>>> with monkeypatch.monkeypatch():
...     mymodule.Hello()
...
Hello, Monkey!
```

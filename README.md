## CODE SWITCHING FROM HINDI ENGLISH MIXED SENTENCES

This is a very simple tkinter ui that takes an input hindi-english romanised sentence and translates it to complete english.

### Pre-requisites:
- Install detectlanguage
```
pip3 install detectlanguage
```
- Install googletrans
```
pip install googletrans==3.1.0a0
```
- Install nltk
```
pip3 install nltk
```

### Exceute:
Use the following command to run the code. This will launch the Tkinter UI window:
```
python3 13_final.py
```

### Limitations:
Any sentence having 'h' rather than 'hai' will not translate it correctly.
Example: 
```
तुम्हारी कोई गलती नहीं ज.इसके मेरे दोष तुम तनाव मत लो 
its not your fault h. its my fault you don't take stress
```

But with 'hai', it is translated correctly:
```
तुम्हारी कोई गलती नहीं हैं . इसका मेरे दोष तुम तनाव मत लो 
You are not at fault. Its my fault you don't stress
```

# Substitution Algorithm

In substitution algorithm, letters or groups of letters are changed systematically throughout the message.

The easiest and most familiar method of substitution cipher is to change the alphabet according to a specified cipher.
In this method, a new encryption alphabet is created and the letters of the password are placed at the beginning of the alphabet.
Then, the letters other than the letters of the word are written in order and a new encryption alphabet is formed.

Then, instead of the letters in the text to be encrypted, the corresponding letters in the encryption alphabet are written and the encrypted text is created.

<div align="center">
  
| Alphabet | Letters |
|:---------------:|:----------------------------------------------------------------------------:|
| Normal Alphabet |` a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z `|
| Cipher Alphabet |` h  e  l  l  o  a  b  c  d  f  g  i  j  k  m  n  p  q  r  s  t  u  v  w  x  y `|

</div>

```

e.g. for "Text to be encrypted" 

  The encryption code will first clarify the text and reduce it to "texttobeencrypted".
  Then it will replace all letters in the text with the corresponding letters of the alphabet in the cipher alphabet.

  Such As ->
              t --> s
              e --> o
              x --> w
              t --> s
              ...
              d --> l

  And turn into "taxttneaamlryptao"

```

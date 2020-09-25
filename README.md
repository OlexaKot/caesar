# Caesar Cipher
# Information
The Caesar Cipher is a substitution cipher named after <a href="https://en.wikipedia.org/wiki/Julius_Caesar">Julius Caesar</a>, who used it in his private correspondence.

For more information about this cipher <a href="https://en.wikipedia.org/wiki/Caesar_cipher">click here</a>.

# Usage
## Encryption
To encrypt a message, use the encrypt() function that takes in two arguments: the plaintext (a string) and the key (integer) and outputs the ciphertext.

Example:
```
>>> encrypt("Hello World!", 9)
'Qnuux Fxaum!'
```
## Decryption
To decrypt a message, use the decrypt() function that likewise takes in two arguments: the ciphertext (a string) and the key (integer) and outputs the plaintext.

Example:
```
>>> decrypt("Qtwjr nuxzr itqtw xny frjy", 5)
'Lorem ipsum dolor sit amet'
```
## Brute-force attack
To crack a message with brute force, use the crack() function that takes in one single argument which is the ciphertext (a string) and outputs every possible variation of the message (26 variations) where only one of 26 variations is the plaintext of the message.

Example:
```
>>> crack("Lzak ak s kwujwl ewkksyw.")
+0 Lzak ak s kwujwl ewkksyw.
+1 Mabl bl t lxvkxm fxlltzx.
+2 Nbcm cm u mywlyn gymmuay.
+3 Ocdn dn v nzxmzo hznnvbz.
+4 Pdeo eo w oaynap iaoowca.
+5 Qefp fp x pbzobq jbppxdb.
+6 Rfgq gq y qcapcr kcqqyec.
+7 Sghr hr z rdbqds ldrrzfd.
+8 This is a secret message.
+9 Uijt jt b tfdsfu nfttbhf.
+10 Vjku ku c ugetgv oguucig.
+11 Wklv lv d vhfuhw phvvdjh.
+12 Xlmw mw e wigvix qiwweki.
+13 Ymnx nx f xjhwjy rjxxflj.
+14 Znoy oy g ykixkz skyygmk.
+15 Aopz pz h zljyla tlzzhnl.
+16 Bpqa qa i amkzmb umaaiom.
+17 Cqrb rb j bnlanc vnbbjpn.
+18 Drsc sc k combod wocckqo.
+19 Estd td l dpncpe xpddlrp.
+20 Ftue ue m eqodqf yqeemsq.
+21 Guvf vf n frperg zrffntr.
+22 Hvwg wg o gsqfsh asggous.
+23 Iwxh xh p htrgti bthhpvt.
+24 Jxyi yi q iushuj cuiiqwu.
+25 Kyzj zj r jvtivk dvjjrxv.
```

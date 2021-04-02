
const alphabet = "abcdefghijklmnopqrstuvwxyz";

function encrypt(plaintext, key) {
    // Defining the variables
    let ciphertext = "";

    // Encryption
    for (iterator = 0; iterator < plaintext.length; iterator++) {
        let currentCharacter = plaintext.charAt(iterator);
        let isUpper = false;
        if (alphabet.includes(currentCharacter.toLowerCase()) == true) {

            // Checking if the current letter is uppercase
            if (alphabet.includes(currentCharacter) == false) {
				isUpper = true;
			}

            currentCharacter = currentCharacter.toLowerCase();
            oldIndex = alphabet.indexOf(currentCharacter);
            newIndex = (oldIndex + key) % 26;
            encryptedLetter = alphabet.charAt(newIndex);


            if (isUpper == true) {
                encryptedLetter = encryptedLetter.toUpperCase();
            }

            ciphertext += encryptedLetter;
        }

        else {
			ciphertext += currentCharacter;
		}
    }
    console.log(ciphertext);
}

function decrypt(ciphertext, key) {
    // Defining the variables
    let plaintext = "";

    // Decryption
    for (iterator = 0; iterator < ciphertext.length; iterator++) {
        let currentCharacter = ciphertext.charAt(iterator);
        let isUpper = false;
        if (alphabet.includes(currentCharacter.toLowerCase()) == true) {

            // Checking if the current letter is uppercase
            if (alphabet.includes(currentCharacter) == false) {
				isUpper = true;
			}

            currentCharacter = currentCharacter.toLowerCase();
            oldIndex = alphabet.indexOf(currentCharacter);
            newIndex = oldIndex - key;
            while (newIndex < 0) {
				newIndex += 26;
			}
            decryptedLetter = alphabet.charAt(newIndex);


            if (isUpper == true) {
                decryptedLetter = decryptedLetter.toUpperCase();
            }

            plaintext += decryptedLetter;
        }

        else {
			plaintext += currentCharacter;
		}
    }
    console.log(plaintext);
}



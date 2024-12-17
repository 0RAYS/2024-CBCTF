import { promptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private inputValue: string = 'CBCTF{Welcome_to_CBCTF_2024}';
  build() {
    Column() {
      TextInput({
        placeholder: 'input flag'
      }).margin({ top: 20 })
        .onSubmit((EnterKeyType)=>{
          console.info(EnterKeyType+'[2341994810, 798981539, 2235011828]')
        })
        .onChange((value: string) => {
          this.inputValue = value;
        })

      Button('Check')
        .width(150)
        .margin({ top: 20 })
        .onClick(() => {
          let ooooo: boolean = this.inputValue.length === 26
          let first: string = this.inputValue.substring(0, 6)
          let nnn: string = this.inputValue.substring(6,13)
          let sss: string = this.inputValue.substring(13,this.inputValue.length - 1)
          let oo: number = parseInt(nnn)
          let ooo: boolean = validateNumber(oo);
          let iii: string = deS("7a747160774b",nnn)
          let o: boolean = first === iii
          //let ppp: string = de([505481640, 1884229320, 1556615705],[883967, 8556999, 116847, 926247])
          let lll: number[] = EN(sss,[883967, 8556999, 116847, 926247],oo)
          let oooo: boolean = AE(lll,[2341984810, 799981539, 2235051828])

          if (o && ooo && oooo && ooooo) {
            showToastMessage('Correct flag!', 1000);
          } else {
            showToastMessage('Error!', 1000);
          }
        });
    }
    .padding(20);
  }
}

function showToastMessage(message: string, duration: number): void {
  try {
    promptAction.showToast({
      message: message,
      duration: duration
    });
  } catch (error) {
    console.error(`showToast args error code is ${error.code}, message is ${error.message}`);
  }
}

function digitSum(num: number): number {
  const digits = num.toString().split('');
  return digits.reduce((sum, digit) => sum + parseInt(digit), 0);
}

function isDigitPrime(digit: number): boolean {
  const primeDigits = [2, 3, 5, 7];
  return primeDigits.includes(digit);
}

function isPrime(num: number): boolean {
  if (num <= 1) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
}

function validateNumber(num: number): boolean {
  const numStr = num.toString();
  const digits = numStr.split('').map((digit) => parseInt(digit));
  const uniqueDigits = new Set(digits);

  return (
    isPrime(num) &&
      uniqueDigits.size === 7 &&
      digitSum(num) === 25 &&
      digits[0] % 2 === 1 &&
    isDigitPrime(digits[digits.length - 1]) &&
      (num + 375924).toString().length === 8
  );
}


function mx(sum: number, y: number, z: number, p: number, e: number, key: number[]): number {
  return (((z >>> 5 ^ y << 2) + (y >>> 3 ^ z << 4)) ^ ((sum ^ y) + (key[(p & 3) ^ e] ^ z)));
}

function en(v: number[], n: number, key: number[],d: number): number[] {
  let rounds: number;
  let sum: number;
  let z: number;
  let y: number;
  let e: number;

  if (n > 1) {
    rounds = Math.floor(13 + 52 / n);
    sum = 0;
    z = v[n - 1];
    while (rounds-- > 0) {
      sum = (sum + d) >>> 0;
      e = (sum >>> 2) & 3;
      for (let p = 0; p < n - 1; p++) {
        y = v[p + 1];
        z = v[p] = (v[p] + mx(sum, y, z, p, e, key)) >>> 0;
      }
      y = v[0];
      z = v[n - 1] = (v[n - 1] + mx(sum, y, z, n - 1, e, key)) >>> 0;
    }
  } else if (n < -1) {
  }

  return v;
}

function strToUint32List(s: string): number[] {
  while (s.length % 4 !== 0) {
    s += '\0';
  }
  const result: number[] = [];
  for (let i = 0; i < s.length; i += 4) {
    const chunk = s.slice(i, i + 4);
    const value = chunk
      .split('')
      .reduce((acc, char, index) => acc + (char.charCodeAt(0) << (8 * index)), 0);
    result.push(value >>> 0);
  }
  return result;
}

function EN(data: string, key: number[],d: number): number[] {
  const v = strToUint32List(data);
  return en(v, v.length, key,d);
}

function deS(encryptedString: string, key: string): string {

  let decrypted: string[] = [];
  let keyLength = key.length;

  for (let i = 0; i < encryptedString.length; i += 2) {
    let hexChar = encryptedString.substring(i, i + 2);

    let decryptedChar = parseInt(hexChar, 16) ^ key.charCodeAt((i / 2) % keyLength);
    decrypted.push(String.fromCharCode(decryptedChar));
  }

  return decrypted.join('');
}

function AE(arr1: number[], arr2: number[]): boolean {
  if (arr1.length !== arr2.length) {
    return false;
  }
  return arr1.every((value, index) => value === arr2[index]);
}






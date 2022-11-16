Airbnb-clone with nomad coder

but with pipenv instead poetry
()

{
"name": "TEST_ROOM2",
"country": "한국",
"city": "서울",
"price": 1000,
"rooms": 2,
"toilets": 2,
"description": "DRF is great!",
"address": "123",
"pet_friendly": true,
"category": 2,
"amenities": [1, 2],
"kind": "private_room"
}

{
"name": "experience test",
"price": 6,
"address": "Seoul",
"start": "18:00:00",
"end": "00:00:00",
"category": 1,
"perk": 1
}

### Typescript

typescript -> javascript 어떤 오류가 있는지 미리 안 뒤 변환한다.

typescript가 type을 추론해준다. -> let a = 2
명시적으로 type을 지정해 줄 수도 있다. -> let a:number[] = []

#### Types

- `type Player : {name:string, age?:number}` -> alias 타입 생성, ?: 객체에서 필수가 아님을 표시
- `const chanhi : Player = {name:"chanhi"}` -> age가 없어도 됨
- `function playerMaker(name: string) : Player {return{name}}` -> 함수 뒤에 인수에 대한 tpye을 지정
- `const names: readonly string[] = ["a", "b"]` -> 배열 안을 바꾸게 되는 작업은 할 수 없음
- unknown -> 이 type으로 지정하게 되면 if문으로 type을 확인하기 전까진 변수로 사용할 수 없음
- void -> 어떤것도 return하지 않음
- never -> 해당 되는 것은 실행되지 않음

#### Function

- call signatures -> 함수의 type 지정 -> `type Add = (a:number, b:number) => number;`
- Overloading -> 하나의 type이 여러개의 call signatures를 가질 때 발생함
- Polymorphism -> 다형성, generics, 여러타입을 받아서 추측하여 지정한다.
- generics : 여러가지의 타입을 미리 지정하지 않고 생성이 될 때 자동으로 type을 정해주는 기법

```typescript
type SuperPrint = { <T>(arr: T[]): T };
const superPrint: SuperPrint = (arr) => {
  return arr[0];
};
const a = superPrint([1, 2, 3]);
const b = superPrint([true, false, true]);
const c = superPrint(["a", "b"]);
const d = superPrint([1, 2, "a", "b", true]);
```

#### Classes

```typescript
abstract class User {
  constructor(
    private firstname: string,
    private lastname: string,
    public nickname: string
  ) {}
  getFullname() {
    return `${this.firstname} ${this.lastname}`;
  }
}

class Player extends User {}

const chanhi = new Player("chanhi", "jung", "chanhi");
chanhi.getFullName();
```

-java, c# 과 같은 객체지향형 언어의 class와 매우 유사함

#### Interfaces

-object의 모양을 특정함 -오직 object를 위해서만 사용됨

```typescript
interface User {
  name: string;
}
interface Player extends User {}

const chanhi: Player = {
  name: "chanhi",
};
```

- 위아래 둘다 같은 기능을 함

```typescript
type User = {
  name: string;
};
type Player = User & {};

const chanhi: Player = {
  name: "chanhi",
};
```

- 이 두가지 방법은 모두 허용되며 자유롭게 선택하면 됨
- 다만 type의 경우는 재선언이 불가하다. (interface는 가능)

```typescript
interface SStorage {
  [key:string]: T
}

class LocalStorage<T> {
  private storage: SStorage<T> = {}
  set(key:string, value:T){
    this.storageg[key] value:
  }
  remove(key:string){
    delete this.storageg[key]
  }
  get(key:string):T {
    return thin.storageg[key]
  }
  clear(){
    thin.storageg = {}
  }
}

const stringStorage = new LocalStorage<string>()

```

- interface + class + 다형성

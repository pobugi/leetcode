class ArrayWrapper {
    private nums: number[];

    constructor(nums: number[]) {
        this.nums = nums;
    }

    valueOf(): number {
        return this.nums.reduce((accumulator, currValue) => accumulator + currValue, 0);
    }

    toString(): string {
        return `[${this.nums.join(",")}]`;
    }
};


const obj1 = new ArrayWrapper([1, 2]);
const obj2 = new ArrayWrapper([3, 4]);
console.log(Number(obj1) + Number(obj2));
console.log(String(obj1) + String(obj2));
console.log(obj1.valueOf() + obj2.valueOf());
console.log(obj1.toString(), obj2.toString());
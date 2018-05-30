// smoke test
const gc = require('./converter');

describe("smoke test", () => {
	it("can blow smoke",() => {
		expect(true).toBe(true);
	});
});

//test conversion of grade averages
describe("A grade average calculator", () => {

	it("can average multiple grades", () => {
		expect(gc.gradeAverage(0,0,0)).toBe(0);
		expect(gc.gradeAverage(60, 80, 90)).toBe(81);
		expect(gc.gradeAverage(50, 60, 80)).toBe(68);
	});

	it("can convert average grade to letter grade", () => {
		expect(gc.convertNumberToGrade(92)).toBe("A");
		expect(gc.convertNumberToGrade(84)).toBe("B");
		expect(gc.convertNumberToGrade(73)).toBe("C");
		expect(gc.convertNumberToGrade(66)).toBe("D");
	});
	
	it("can output users final grade in a sentence", () => {
		expect(gc.getMessage(97, "A")).toBe("The student's grade average is 97. They will recieve a A in the class.");
		expect(gc.getMessage(85, "B")).toBe("The student's grade average is 85. They will recieve a B in the class.");
		expect(gc.getMessage(71, "C")).toBe("The student's grade average is 71. They will recieve a C in the class.");
		expect(gc.getMessage(62, "D")).toBe("The student's grade average is 62. They will recieve a D in the class.");
		expect(gc.getMessage(15, "F")).toBe("The student's grade average is 15. They will recieve a F in the class.")
	});
});
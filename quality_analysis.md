# Software Quality Analysis: User Validator Module
**Project:** SE Laboratory Midterm Exam  

---

## 1. Relevant ISO/IEC 25010 Quality Attributes

For the **UserValidator** module, the following two quality attributes are the most relevant:

### A. Security

* **Relevance:** Since this module handles user credentials (usernames and passwords), security is the primary attribute. 
* **Implementation:** The module enforces **Input Validation/Error Handling** by requiring alphanumeric characters for usernames, and a minimum length of 8 characters for passwords to ensure strong credential data.

### B. Functional Suitability

* **Relevance:** The main logic of this module is to efficiently register users, and ensure the credentials are correct before logging them in.
* **Implementation:** The `UserValidator` ensures input by checking for duplicate usernames. As a result, the system maintains data integrity, which is an important requirement for any common authentication system.

---

## 2. How Automated Testing Supports These Attributes
The test cases located in `tests/test_module.py` serves as references for the attributes mentioned:

* **Security:** The `test_register_negative_short_password` and `test_register_negative_invalid_chars` cases are meant to attempt to break the security rules. By ensuring these tests pass (meaning the code successfully blocks the invalid input), this confirms that the precautions are active and working.
* **Functional Suitability:** The `test_register_positive` case confirms that the system works for valid users, while the `test_register_edge_duplicate` case ensures the system prevents data redundancy.
  
---

## 3. How CI/CD Improves Reliability

Implementing the **CI Pipeline** enhances the reliability of the software in several ways:

* **Prevention of Human Error:** At times when developers forget to run tests locally before pushing, reliability gets compromised. With a CI pipeline, it automates this process ensuring every single line of code is verified by a machine before it gets pushed, making it easier for developers.
* **Continuous Verification:** As projects grow, new code changes might accidentally break old features. The CI pipeline helps developers catch these errors immediately, ensuring the code in the "main" project branch does not completely break. Additionally, it will also show the reason why errors are occurring in the first place.

---

> **Prepared by:** Jhoanna Alexandra C. De La Paz  
> **Course:** Software Engineering (LAB)

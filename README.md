# Secure Backend Auth Toolkit

## Summary

A reference implementation of security-hardened authentication and data-protection patterns for backend systems, built with Python and FastAPI. This project reflects engineering practices applied across backend work — encryption, secure session handling, and defensive coding patterns — that inform how I approach security review more broadly, including in protocol-level and smart contract auditing.

**Status:** Active development

## Features

- JWT-based authentication with proper expiry and refresh-token handling
- Password hashing via Argon2 (memory-hard, resistant to GPU cracking)
- AES-256 encryption for sensitive data at rest
- Input validation and rate-limiting patterns to reduce common attack surface
- Structured for easy security review — clear separation of auth logic, crypto operations, and request handling

## Tech Stack

- **Backend:** Python, FastAPI, PostgreSQL
- **Security:** `argon2-cffi`, `pyjwt`, `cryptography` (AES-256-GCM)
- **Testing:** pytest, with test cases covering auth edge cases and token expiry behavior

## Why This Repo Exists

Good protocol and smart contract security research is built on solid fundamentals in applied cryptography and secure system design. This toolkit is where I apply and test those fundamentals in a traditional backend context — the same verification-first mindset carries over to my ZK protocol and smart contract security research.

## Related Work

- [zkVerify BN254 Point-Validation Research](https://github.com/Mustafa-SeniorDev/zkVerify-BN254-PointValidation-Research)
- [Zeko Protocol Fee-Payer Authorization Research](https://github.com/Mustafa-SeniorDev/Zeko-Protocol-FeePayer-Authorization-Research)
- [ZK-Verifier Point-Validation Checker](https://github.com/Mustafa-SeniorDev/ZK-Verifier-PointValidation-Checker)

## Author

**Mustafa Ramadhani** — Software Engineer & Independent Security Researcher, Dar es Salaam, Tanzania
📫 Mustafarama405@gmail.com · [LinkedIn](https://www.linkedin.com/in/mustafa-ramadhani-59394b354)

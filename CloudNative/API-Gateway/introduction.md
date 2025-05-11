# API Gateway — Deep Dive

## 1. What is an API Gateway?

An **API Gateway** is a **server layer** that acts as an **entry point** for client requests to access one or more backend services (usually in microservices architectures).

Think of it as:

> The **traffic controller** and **security guard** for all incoming API calls.

Instead of clients calling backend services directly, **all traffic goes through the API Gateway**, which then routes, processes, and manages requests.

---

## 2. How Does It Work?

**Flow:**

1. **Client sends a request**  
   → Could be from a browser, mobile app, IoT device, etc.

2. **Gateway intercepts the request**  
   - Checks authentication/authorization.
   - Validates request structure.
   - Enforces rate limits, throttling, quotas.
   
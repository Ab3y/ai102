# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in this repository, please report it responsibly.

**Do not** create a public GitHub issue for security vulnerabilities.

Instead, please email the repository maintainer directly.

## Security Best Practices

When using the code samples in this repository:

- **Never commit API keys, secrets, or connection strings** to source control
- Use `.env` files for local development (already in `.gitignore`)
- Use Azure Key Vault and managed identities in production
- Rotate API keys regularly
- Follow the principle of least privilege for RBAC assignments

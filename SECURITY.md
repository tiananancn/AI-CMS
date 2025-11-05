# Security Policy

## Supported Versions

We actively support the following versions of AI-CMS with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 3.0.x   | :white_check_mark: |
| 2.5.x   | :white_check_mark: |
| 2.0.x   | :white_check_mark: |
| < 2.0   | :x:                |

## Reporting a Vulnerability

We take the security of AI-CMS seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report security vulnerabilities by:

1. **Email**: Send an email to [your-email@example.com] with:
   - Subject: "Security Vulnerability - AI-CMS"
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact

2. **GitHub Security Advisories**: Alternatively, you can report through GitHub's private vulnerability reporting feature.

### What to Include

Please provide as much information as possible to help us understand and reproduce the issue:

- Type of vulnerability (XSS, SQL injection, CSRF, etc.)
- Full paths of source file(s) related to the manifestation of the vulnerability
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue
- Any other information you think would be helpful

### Response Timeline

- **Acknowledgment**: We will acknowledge receipt of your vulnerability report within 48 hours
- **Initial Assessment**: We will provide an initial assessment within 5 business days
- **Resolution Timeline**: We will aim to resolve critical vulnerabilities within 30 days, and non-critical vulnerabilities within 90 days

### Security Measures in Place

- File upload validation and sanitization
- SQL injection protection via SQLAlchemy ORM
- XSS protection via Jinja2 auto-escaping
- CSRF protection recommended for production deployment
- Session-based authentication

### Best Practices for Deployment

To ensure your AI-CMS deployment is secure:

1. **Change Default Credentials**: Change the default admin username and password before deployment

2. **Use HTTPS**: Always use HTTPS in production to encrypt data in transit

3. **Database Security**:
   - Use a production-grade database (PostgreSQL/MySQL) instead of SQLite
   - Enable database encryption
   - Regular backups

4. **Environment Variables**:
   - Store sensitive configuration in environment variables
   - Never commit `.env` files to version control

5. **File Permissions**:
   - Ensure proper file permissions on the server
   - Limit write access to upload directories

6. **Regular Updates**:
   - Keep dependencies updated
   - Monitor security advisories
   - Apply security patches promptly

7. **Server Configuration**:
   - Use a reverse proxy (Nginx/Apache)
   - Enable gzip compression
   - Set up rate limiting
   - Configure firewall rules

8. **Monitoring**:
   - Set up logging and monitoring
   - Monitor for unusual activity
   - Regular security audits

### Known Security Considerations

1. **Default Admin Credentials**: The default credentials (`admin/admin`) must be changed before production use

2. **SQLite Database**: For production use, replace SQLite with a more robust database solution

3. **File Uploads**: While file uploads are validated, ensure server-level restrictions are also in place

4. **Session Security**: Implement proper session timeout and secure session management

### Recognition

We appreciate your efforts to responsibly disclose security vulnerabilities. If your report leads to a security fix, we will acknowledge your contribution (unless you prefer to remain anonymous).

## Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Flask Security](https://flask.palletsprojects.com/en/latest/security/)
- [Python Security Guidelines](https://python.org/dev/security/)

Thank you for helping keep AI-CMS and its users safe!

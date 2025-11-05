# Contributing to AI-CMS

Thank you for your interest in contributing to AI-CMS! This document provides guidelines for contributing to the project.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct:
- Be respectful and inclusive
- Focus on constructive feedback
- Show empathy towards other contributors

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues as you might find that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed and explain what behavior you expected**
- **Include screenshots if applicable**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and explain the behavior you expected**
- **Explain why this enhancement would be useful**

### Pull Requests

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Development Setup

### Prerequisites

- Python 3.7+
- pip

### Setting up the development environment

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/cms.git
cd cms

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run tests with coverage
python -m pytest --cov=.
```

## Coding Standards

### Python Code Style

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for all public functions and classes
- Maximum line length: 88 characters (Black formatter)

### HTML Templates

- Use meaningful class names
- Comment complex template logic
- Follow Bootstrap 5 best practices

### JavaScript

- Use ES6+ features
- Add JSDoc comments for functions
- Keep functions small and focused
- Use meaningful variable names

### CSS

- Follow BEM naming methodology when possible
- Use Bootstrap classes first, custom CSS second
- Comment complex selectors

## Commit Messages

Use clear and descriptive commit messages:

```
type(scope): brief description

Longer description if needed

Fixes #123
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

## Documentation

- Update documentation for any changed functionality
- Add docstrings to new functions and classes
- Update README.md if needed
- Add inline code comments for complex logic

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

If you have any questions, please feel free to open an issue or contact the maintainers.

Thank you for contributing to AI-CMS! 🎉

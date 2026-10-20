FROM python:3.12-alpine
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 PORT=8080
WORKDIR /srv/muni-cloud
COPY --chown=10001:10001 app/ ./app/
USER 10001:10001
EXPOSE 8080
HEALTHCHECK --interval=20s --timeout=3s --start-period=5s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health', timeout=2)"
CMD ["python", "app/server.py"]

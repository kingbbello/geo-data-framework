# Geo Data Framework

A comprehensive framework for handling and processing geographical data, built with Ruby on Rails and PostgreSQL/PostGIS.

## Project Structure

The project consists of three main services:

- **Web Application**: A Ruby on Rails application serving as the main interface
- **Scraper**: A service for collecting and processing geographical data
- **Database**: PostgreSQL with PostGIS extension for spatial data storage and processing

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd geo-data-framework
   ```

2. Start the services:
   ```bash
   docker-compose up
   ```

The services will be available at:
- Web Application: http://localhost:3000
- Database: localhost:5432

## Services

### Web Application
- Built with Ruby on Rails
- Serves as the main interface for the application
- Accessible at http://localhost:3000

### Scraper
- Dedicated service for data collection and processing
- Located in the `./scraper` directory

### Database
- PostgreSQL 15 with PostGIS 3.3 extension
- Default credentials:
  - Username: postgres
  - Password: password
  - Database: geo_data
- Accessible at localhost:5432

## Development

The project uses Docker volumes to mount the local directories, allowing for live code changes without rebuilding containers.

### Directory Structure
- `./rails-app`: Contains the Rails application
- `./scraper`: Contains the scraper service
- `docker-compose.yml`: Defines the service configuration

## Data Persistence

The PostgreSQL data is persisted using a Docker volume named `pg_data`.

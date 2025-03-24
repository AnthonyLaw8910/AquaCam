#!/bin/bash
gunicorn app:appplication --bind 0.0.0.0.:5000

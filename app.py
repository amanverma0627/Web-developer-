from flask import Flask, render_template, jsonify, request
from config import config
import os

def create_app(config_name=None):
    """Application factory""" 
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    init_extensions(app)
    
    # Register blueprints
    register_blueprints(app)
    
    # Error handlers
    register_error_handlers(app)
    
    return app

def init_extensions(app):
    """Initialize Flask extensions"""
    pass

def register_blueprints(app):
    """Register Flask blueprints"""
    @app.route('/')
    def index():
        return jsonify({
            'message': 'Welcome to Health Chatbot & Assistant',
            'version': '1.0.0',
            'status': 'running'
        })
    
    @app.route('/health')
    def health_check():
        return jsonify({'status': 'healthy'}), 200

def register_error_handlers(app):
    """Register error handlers"""
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)

# config


# Enable  Flask's debugging features. should be fasle in pruduction
#DEBUG = True

class Config(object):
	"""
	common configurations

	"""

	# put any configuration  here that are common across all the enviroments

class DelevelopmentConfig(Config):
		"""
		Delevepment configurations
		"""

		DEBUG = True
		SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
		"""
			Production configurations

		"""
		DEBUG = False


app_config = {
	'development' : DelevelopmentConfig,
	'production'  : ProductionConfig
}


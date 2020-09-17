package com.schlumberger.clock.config

import java.io.InputStream
import java.util.Properties


/**
 * @author Piyush
 * Utility class to read data from property file
 */
object ReadConfig {

  val prop = new Properties
  val propFileName = "config.properties"

  val inputStream: InputStream = getClass.getClassLoader.getResourceAsStream(propFileName)
  prop.load(inputStream)

  def getConfig(key: String): String = {
    prop.getProperty(key)
  }
}

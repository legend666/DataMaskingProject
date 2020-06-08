package mask;

import detect.FinderEngine;

/**
 * A class which implements a masking operation using
 * a FinderEngine
 *
 */

public interface Masker {
	
	/**
	 * initialize the Masker using the FinderEnginer and
	 * a string which provides a pointer for Masker's configuration.
	 * @param engine - FinderEngine
	 * @param configuration -String containing configuration information for
	 * Masker
	 */
	void init (FinderEngine engine, String configuration);
	
	/**
	 * Accepts an input text and mask it.
	 * @param input - text to be masked
	 * @return masked text
	 */
	
	String mask(String input);
}

package detect;


/**
 * Interface for Finders
 * To add a new Java Finder, one needs to implement Finder interface.
 *
 */

public interface Finder {

  /**
   * Name of the Finder
   * @return name of the Finder
   */
  public String getName();
  
  /**
   * Accepts an input value and 
   * returns a collection of sensitive values found in the inputs.
   * @param input - String to be scanned.
   * @return List of sensitive values
   */
  public FinderResult find(String input);
    
}

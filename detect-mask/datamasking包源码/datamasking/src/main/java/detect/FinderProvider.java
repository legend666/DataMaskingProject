package detect;

import java.util.List;
/**
 * A provider for Finders.
 * DefaultFinderProvider provides finders read from finders.xml
 */
public interface FinderProvider {
	
	/**
	 * 
	 * @return a list of Finders
	 */
	List<Finder> getFinders();
}

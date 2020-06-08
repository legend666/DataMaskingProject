package pattern;


import detect.Finder;
import detect.FinderResult;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

public class RegexFinder implements Finder {
	static final Log LOG = LogFactory.getLog(RegexFinder.class);
	public static final int DEFAULT_FLAGS = 
			Pattern.CANON_EQ | Pattern.CASE_INSENSITIVE | Pattern.MULTILINE;

	private String name;
	Pattern pattern;
	
	public RegexFinder() {}

	/**
	 * Construct a Regular expression Based Finder using a pattern and default flags.
	 * @param name - name of the Finder
	 * @param pattern - pattern of the regular expression.
	 */
	public RegexFinder(String name, String pattern) {
		this(name, pattern,DEFAULT_FLAGS);
	}

	/**
	 * Construct a Regular expression Based Finder using pattern and flags.
	 * @param name - name of the Finder
	 * @param pattern - pattern of the regular expression.
	 * @param flags - Flags to be used while compiling the pattern.
	 */
	public RegexFinder(String name, String pattern, int flags) {
		this.name = name;
		this.pattern = Pattern.compile(pattern, flags);
	}

	/**
	 * set the name of the Finder
	 * @param name
	 */
	public void setName(String name) {
		this.name = name;
	}

	/**
	 * get Finder's name.
	 */
	public String getName() {
		return name;
	}

	/**
	 * set the Pattern
	 * @param pattern
	 */
	public void setPattern(Pattern pattern) {
		this.pattern = pattern;
	}

	/**
	 * Get Pattern.
	 */
	public Pattern getPattern() {
		return pattern;
	}

	/**
	 * Scan the list of inputs using the finders.
	 * Return a list of actual matched values.
	 * @return a list of matches 
	 */
	public FinderResult find(String input) {
		List<String> matches = new ArrayList<>();
		Matcher matcher = pattern.matcher(input);
		while (matcher.find()) {
			matches.add(input.substring(matcher.start(), matcher.end()));
		}
		return new FinderResult(matches, replace(input,""));
	}
	

	static String removeCommas(String match) {
		if (match.endsWith(",")) {
			match = match.substring(0, match.length() - 1);
		}
		if (match.startsWith(",")) {
			match = match.substring(1);
		}
		return match;
	}

	private String replace(String input, String replacement) {
		Matcher matcher = pattern.matcher(input);
		return matcher.replaceAll(replacement);
	}

}
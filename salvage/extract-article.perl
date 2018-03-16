#! /usr/bin/perl
use strict;
use warnings;
use v5.20.2;
use Data::Dump qw/dump/;
use File::Slurper qw/read_text/;
use Getopt::Long;
use autodie qw(:all);
use Log::Any qw($log);
use Log::Dispatch;
use Log::Any::Adapter;
use HTML::TreeBuilder;

sub init_logging {
    # Send all logs to Log::Dispatch
    my $dispatch_logger = Log::Dispatch->new(
        outputs => [
            [ 'Screen', min_level => 'debug', newline => 1 ],
        ],
    );
    Log::Any::Adapter->set('Dispatch', dispatcher => $dispatch_logger);
}

init_logging();
$log->debugf("arguments are: %s", "foo");


my $data   = "file.dat";
my $length = 24;
my $verbose;

# This will pull out some content and put it into an XHTML container.
# You still need to run tidy on the result to fix it afterwards.

binmode(STDOUT, ':utf8');

GetOptions ("length=i" => \$length,    # numeric
            "file=s"   => \$data,      # string
            "verbose"  => \$verbose)   # flag
    or die("Error in command line arguments\n");

my $prelude = '<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:epub="http://www.idpf.org/2007/ops">
<head>
<title>Conforming HTML5 Template</title>
</head>
<body>
';

my $postscript = '
</body>
</html>
';

sub main {
    for my $arg (@_) {
        my $tree = HTML::TreeBuilder->new(ignore_unknown => 0);

        open my $fh, '<:utf8', $arg;

        $tree->parse_file($fh);
        $tree->eof;
        $tree->elementify;
        my $first_article = $tree->find('article');
        say $prelude;
        say $first_article->as_HTML('', '  ');
        say $postscript;

        close $fh
    }
}

main @ARGV;

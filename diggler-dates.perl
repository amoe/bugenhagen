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

GetOptions ("length=i" => \$length,    # numeric
            "file=s"   => \$data,      # string
            "verbose"  => \$verbose)   # flag
    or die("Error in command line arguments\n");

sub main {
    for my $arg (@_) {
        my $content = read_text($arg);
        my $root = HTML::TreeBuilder->new_from_content($content);
        my $first_match = $root->look_down(property => 'article:published_time');

        # We are looking for something like the following.
        # <meta property="article:published_time" content="2016-07-08T15:20:21-05:00"/>

        
        say $arg .  "\t" . $first_match->attr('content');
    }
}

main @ARGV;

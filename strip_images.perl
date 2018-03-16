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
        # my @matches = $root->look_down(class => 'author-photo');
#        my @matches = $root->look_down(_tag => 'img');
#        my @matches = $root->look_down(_tag => 'script');
        my @matches = $root->look_down(_tag => 'iframe');

        for my $match (@matches) {
            $match->delete();
        }

        say $root->as_HTML;
    }
}

main @ARGV;
